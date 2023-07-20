#pip install cx_freeze
import cx_Freeze
executables =[
    cx_Freeze.Executable(script="mario.py", icon="icone.ico")
]
cx_Freeze.setup(
    name = "Mario World",
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["fundo.jpg",
                            "icone.png",
                            "mario.png",
                            "trilha.mp3"]
        }
    }, executables = executables
)

#py setup.py build
#py setup.py bdist_msi