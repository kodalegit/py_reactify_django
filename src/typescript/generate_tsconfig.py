import json


def generate_tsconfig():
    tsconfig = {
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
        "exclude": ["node_modules", "build"],
    }

    # Write the tsconfig to a file
    with open("tsconfig.json", "w") as file:
        json.dump(tsconfig, file, indent=2)

    print("Generated tsconfig.json successfully")
