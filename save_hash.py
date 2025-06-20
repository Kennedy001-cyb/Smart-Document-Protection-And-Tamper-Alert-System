import hashlib

def generate_hash(file_path):
    with open(file_path, "rb") as f:
        content = f.read()
        return hashlib.sha256(content).hexdigest()

file_path = "C:\\Users\\USER\\Desktop\\ProtectedDocs\\List_of_Freshly_Employed_Personnel_and_Their_Roles.docx"
original_hash = generate_hash(file_path)

with open("hash.docx", "w") as h:
    h.write(original_hash)

print("Original file hash saved.")