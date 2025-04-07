from fpdf import FPDF
from fpdf.enums import Align

class PDF(FPDF):
    def header(self):
        # Setting font: courier bold 45
        self.set_font("courier", style="B", size=45)
        # Adding line break to bring title down
        self.write_html("<br>")
        # Calculating width of title and setting cursor position:
        width = self.get_string_width(self.title) + 6
        self.set_x((210 - width) / 2)
        # Setting colors for frame, background and text:
        self.set_draw_color(0, 51, 102)
        self.set_fill_color(204, 255, 255)
        self.set_text_color(128, 0, 0)
        # Setting thickness of the frame (1 mm)
        self.set_line_width(1)
        # Printing title:
        self.cell(
            width,
            21,
            self.title,
            border=1,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
            fill=True,
        )
        # Performing a line break:
        self.ln(10)

    def footer(self):
        # Setting position at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("courier", style="I", size=8)
        # Setting text color to gray:
        self.set_text_color(128)
        # Printing page number
        self.cell(0, 10, "Artwork by Brandon Gay", align="C")

    def write_text(self):
        self.set_font("helvetica", style="B", size=22)
        self.set_text_color(255, 255, 255)
        self.multi_cell(
            0, 
            None, 
            "\n\n\n\n\n\n\n\nBRANDON GAY\n\nCONQUERED CS50", 
            align=Align.C
            )


def main():
    pdf = PDF()
    pdf.set_title("CS50 Shirtificate")
    pdf.set_page_background((255, 255, 180))
    pdf.add_page()
    pdf.image("shirtificate.png", Align.C, 75, 150, 0)
    pdf.write_text()
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()



