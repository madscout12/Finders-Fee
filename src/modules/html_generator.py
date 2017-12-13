class HTMLGenerator:
    def __init__(self):
        self.css = "<style type=\"text/css\">\n \
.tg  {border-collapse:collapse;border-spacing:0;border-color:#aaa;margin:0px auto;}\n \
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#aaa;color:#333;background-color:#fff;}\n \
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#aaa;color:#fff;background-color:#f38630;}\n \
.tg .tg-even{background-color:#FCFBE3; color:#333333}\n \
.tg .tg-odd{background-color:#FFFFFF; color:#333333}\n \
</style>\n"

        self.table_open = "<table class=\"tg\">\n"
        self.table_close = "</table>\n"

        self.row_open = "<tr>\n"
        self.row_close = "</tr>\n"

        self.header_row_cell = "<th class=\"tg-031e\">{}</th>"
        self.odd_row_cell = "<th class=\"tg-odd\">{}</th>"
        self.even_row_cell = "<th class=\"tg-even\">{}</th>"

    def print_file(self, data, path):
        with open(path, "w") as file:
            file.write(self._generate_html(data))

    def _generate_html(self, data):
        output = self.css
        output += self.table_open

        output += self.row_open
        output += self.header_row_cell.format("Count")
        for key in sorted(data[0]):
            output += self.header_row_cell.format(key)
        output += self.row_close

        for num in range(0, len(data)):
            output += self.row_open

            cell = self.even_row_cell if num % 2 == 0 else self.odd_row_cell

            output += cell.format(str(num))
            for key in sorted(data[num]):
                output += cell.format(data[num][key])
            output += self.row_close

        output += self.table_close
        return output
