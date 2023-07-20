#pip install cx_freeze
import cx_Freeze
executables =[
    cx_Freeze.Executable(script="main.py", icon="meteoro.ico")
]
cx_Freeze.setup(
    name = "Mario World",
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["back.jpg",
                            "nave.png",
                            "meteoro.png",
                            "meteoro.mp3",
                            "trilha.mp3"
                            ]
        }
    }, executables = executables
)

#py geraSetup.py build
#py geraSetup.py bdist_msi