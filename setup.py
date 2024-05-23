from cx_Freeze import setup, Executable

setup(
    name="Taiga Tournament",
    version="1.0",
    description="Programa para organizar torneos",
    executables=[Executable("TaigaTournament.pyw", base="Win32GUI")]
)