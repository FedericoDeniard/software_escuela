from cx_Freeze import setup, Executable

# Lista de archivos a incluir en el archivo ejecutable
includefiles = ['data/']

# Configuración de cx_Freeze
build_exe_options = {
    "include_files": includefiles,
    "zip_include_packages": ["*"],
    "zip_exclude_packages": [],
}

setup(
    name="main",
    version="1.1",
    description="Software de carga de datos",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py")]
)
