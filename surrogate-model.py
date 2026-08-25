import clr

DWSIM_PATH = r"C:\Users\anany\AppData\Local\Programs\DWSIM"

clr.AddReference(DWSIM_PATH + r"\DWSIM.Interfaces.dll")
clr.AddReference(DWSIM_PATH + r"\DWSIM.FlowsheetBase.dll")
clr.AddReference(DWSIM_PATH + r"\DWSIM.FlowsheetSolver.dll")

print("DWSIM libraries loaded successfully!")
