import base64

input_data = str(input("Path of file (ex:hidden.pdf)"))
output_file = str(input("Path of program: "))
# Encode the PDF file into a string
with open(input_data, "rb") as pdf_file:
    encoded_string = base64.b64encode(pdf_file.read()).decode("utf-8")

with open(output_file, "a") as new_code:
    new_code.write("\n\nimport base64\n\n")
    new_code.write("encoded_pdf = \"" + encoded_string + "\"\n\n")
    new_code.write("# Decode the PDF string back into bytes\n")
    new_code.write("decoded_pdf = base64.b64decode(encoded_pdf)\n\n")
    new_code.write("# Write the decoded PDF bytes into a new file\n")
    new_code.write("with open(\"decoded.pdf\", \"wb\") as pdf_file:\n")
    new_code.write("    pdf_file.write(decoded_pdf)\n")