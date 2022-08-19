import unittest
import uuid

from tests.utilities import IdGenerator
from parameterized import parameterized


class IdGeneratorTests(unittest.TestCase):

    def test_use_default_scope_when_not_specified(self):
        id_generator = IdGenerator()
        self.assertEqual(IdGenerator.default_scope, id_generator.scope)

    @parameterized.expand([
        ["custom-scope"],
        [""]
    ])
    def test_uses_provided_scope(self, scope):
        id_generator = IdGenerator(scope)
        self.assertEqual(scope, id_generator.scope)

    def test_explicit_none_scope_uses_default(self):
        id_generator = IdGenerator(None)
        self.assertEqual(IdGenerator.default_scope, id_generator.scope)

    @parameterized.expand([
        ["default scope", None, IdGenerator.default_scope],
        ["override scope", "new-scope", "new-scope"]
    ])
    def test_generate_scope_and_code(self, _, scope, expected_scope):
        id_generator = IdGenerator()
        gen_entity, gen_scope, gen_code = id_generator.generate_scope_and_code("portfolio", scope=scope)

        self.assertEqual("portfolio", gen_entity)
        self.assertEqual(expected_scope, gen_scope)
        self.assertIsNotNone(gen_code)
        self.assertIsNot("", gen_code)

    def test_generate_scope_and_code_with_scope_prefix(self):
        code_prefix = "abc-"
        id_generator = IdGenerator()
        gen_entity, gen_scope, gen_code = id_generator.generate_scope_and_code("portfolio", code_prefix=code_prefix)

        self.assertEqual("portfolio", gen_entity)
        self.assertEqual(IdGenerator.default_scope, gen_scope)
        self.assertIsNotNone(gen_code)
        self.assertTrue(gen_code.startswith(code_prefix))

    def test_generate_scope_and_code_with_different_entity(self):
        id_generator = IdGenerator()
        entity1, scope1, code1 = id_generator.generate_scope_and_code("portfolio")

        entity2, scope2, code2 = id_generator.generate_scope_and_code("property")

        vals = set(id_generator.pop_scope_and_codes())

        self.assertEqual(2, len(vals))
        self.assertIn((entity1, scope1, code1), vals)
        self.assertIn((entity2, scope2, code2), vals)

    def test_clear_scope_and_code(self):
        id_generator = IdGenerator()
        id_generator.generate_scope_and_code("portfolio")

        vals = id_generator.pop_scope_and_codes()
        self.assertEqual(1, len(list(vals)))

        id_generator.clear()

        self.assertEqual(0, len(list(vals)))

    def test_get_scope_and_code_with_default_scope(self):
        id_generator = IdGenerator()
        entity, scope, code = id_generator.generate_scope_and_code("portfolio")

        val = next(id_generator.pop_scope_and_codes(), None)

        self.assertEqual(scope, val[1])
        self.assertEqual(scope, id_generator.default_scope)

        val = next(id_generator.pop_scope_and_codes(), None)
        self.assertIsNone(val)

    def test_get_scope_and_code_with_specified_scope(self):
        test_scope = "test-scope"
        id_generator = IdGenerator(test_scope)
        entity, scope, code = id_generator.generate_scope_and_code("portfolio")

        val = next(id_generator.pop_scope_and_codes(), None)

        self.assertEqual(scope, val[1])
        self.assertEqual(scope, test_scope)

        val = next(id_generator.pop_scope_and_codes(), None)
        self.assertIsNone(val)

    def test_get_multiple_scope_and_codes(self):
        id_generator = IdGenerator()
        n = 5

        vals = {
            id_generator.generate_scope_and_code("portfolio")
            for _ in range(n)
        }

        gen_vals = set(id_generator.pop_scope_and_codes())
        self.assertEqual(n, len(gen_vals))
        self.assertSetEqual(vals, gen_vals)

    def test_add_scope_and_code(self):
        id_generator = IdGenerator()
        code = str(uuid.uuid4())
        id_generator.add_scope_and_code("portfolio", IdGenerator.default_scope, code)

        val = next(id_generator.pop_scope_and_codes(), None)

        self.assertEqual(IdGenerator.default_scope, val[1])
        self.assertEqual(code, val[2])

    def test_add_scope_and_code_with_specified_scope(self):
        test_scope = "test-scope"
        id_generator = IdGenerator()
        code = str(uuid.uuid4())
        id_generator.add_scope_and_code("portfolio", test_scope, code)

        val = next(id_generator.pop_scope_and_codes(), None)

        self.assertEqual(test_scope, val[1])
        self.assertEqual(code, val[2])

    def test_add_existing_scope_and_code(self):
        id_generator = IdGenerator()
        _, gen_scope, gen_code = id_generator.generate_scope_and_code("portfolio")

        id_generator.add_scope_and_code("portfolio", gen_scope, gen_code)

        gen_vals = set(id_generator.pop_scope_and_codes())
        self.assertEqual(1, len(gen_vals))

    def test_generate_scope_and_code_with_annotations(self):
        id_generator = IdGenerator()
        test_scope = "test-scope"
        annotations = ["val1", "val2"]
        item = id_generator.generate_scope_and_code(
            "portfolio",
            scope=test_scope,
            annotations=annotations
        )

        self.assertEqual("portfolio", item[0])
        self.assertEqual(test_scope, item[1])
        self.assertIsNotNone(item[2])
        self.assertIsNot("", item[2])
        self.assertEqual("val1", item[3])
        self.assertEqual("val2", item[4])

    def test_add_scope_and_code_with_annotations(self):
        id_generator = IdGenerator()
        test_scope = "test-scope"
        test_code = "test-code"
        annotations = ["val1", "val2"]
        item = id_generator.add_scope_and_code(
            "portfolio",
            scope=test_scope,
            code=test_code,
            annotations=annotations
        )

        self.assertEqual("portfolio", item[0])
        self.assertEqual(test_scope, item[1])
        self.assertEqual(test_code, item[2])
        self.assertEqual("val1", item[3])
        self.assertEqual("val2", item[4])
