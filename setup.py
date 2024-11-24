from cx_Freeze import setup, Executable

executables = [Executable("brightness.py", base="Console")]

setup(
    name="BrightnessApp",
    version="1.0",
    description="Una aplicación para controlar el brillo",
    executables=executables
)
