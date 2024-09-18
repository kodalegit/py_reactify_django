from .typescript.generate_tsconfig import generate_tsconfig


def configure_typescript(use_typescript):
    if use_typescript:
        generate_tsconfig()
