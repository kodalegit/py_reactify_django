from unittest import mock
import unittest
import json
from src.reactify_django.typescript.generate_tsconfig import generate_tsconfig


class TestGenerateTsconfig(unittest.TestCase):

    @mock.patch("builtins.open", new_callable=mock.mock_open)
    def test_generate_tsconfig(self, mock_open):
        # Call the function to generate tsconfig
        generate_tsconfig()

        # Define the expected JSON content
        expected_tsconfig = {
            "compilerOptions": {
                "target": "es5",
                "lib": ["dom", "dom.iterable", "esnext"],
                "allowJs": True,
                "skipLibCheck": True,
                "esModuleInterop": True,
                "allowSyntheticDefaultImports": True,
                "strict": True,
                "forceConsistentCasingInFileNames": True,
                "noFallthroughCasesInSwitch": True,
                "module": "esnext",
                "moduleResolution": "node",
                "resolveJsonModule": True,
                "isolatedModules": True,
                "noEmit": True,
                "jsx": "react-jsx",
                "baseUrl": "./",
                "paths": {"@/*": ["src/*"]},
            },
            "include": ["**/*.ts", "**/*.tsx"],
            "exclude": ["node_modules"],
        }

        # Check that open was called with the correct parameters
        mock_open.assert_called_once_with("tsconfig.json", "w")

        # Join all write calls to form the final content
        written_content = "".join(
            call.args[0] for call in mock_open().write.call_args_list
        )

        self.maxDiff = None

        # Check that the file write method was called with the correct content
        self.assertEqual(written_content, json.dumps(expected_tsconfig, indent=2))


if __name__ == "__main__":
    unittest.main()
