

def get_description(em):
    table_content_item = """
    
                    <head>
                        <meta charset="UTF-8">
                        <style type="text/css">
                            .mytable {
                                table-layout: fixed;
                            }
                            .mytable tr td {
                                text-overflow: ellipsis;
                                overflow: hidden;
                                white-space: nowrap;
                            }
                             .a{
                               width: 125px;
                            }
                        </style>
                    </head>
                    <body>
                            <table width="1200px" class="mytable">
                                <tr>
                                    <td class="a">%s</td>
                                    <td title=%s>%s</td>
                                </tr>
                            </table>
                    </body>
                    """

    table_content = ""
    for k, v in em.__dict__.items():
        table_content += table_content_item % (k, v, v)
    return table_content