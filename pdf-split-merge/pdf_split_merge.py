from PyPDF2 import PdfMerger, PdfReader

choice = input("split or merge?: ")

if choice == "merge":
    merger = PdfMerger()
    files = input("Enter PDF names separated by comma: ").split(",")

    for pdf in files:
        merger.append(pdf.strip())

    merger.write("merged.pdf")
    merger.close()

else:
    reader = PdfReader("input.pdf")
    for i, page in enumerate(reader.pages):
        writer = PdfMerger()
        writer.append(reader, pages=(i, i+1))
        writer.write(f"page_{i+1}.pdf")
        writer.close()
