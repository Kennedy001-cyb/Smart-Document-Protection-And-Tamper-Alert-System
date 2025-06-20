Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c python C:\Users\User\Desktop\ProtectedDocs\watcher.py", 0
Set WshShell = Nothing