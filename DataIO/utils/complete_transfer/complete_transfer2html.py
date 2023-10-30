""" Function to complete the transfer to an html.extra_files_path by modifying the html file. """

def _complete_transfer2html(fpath):
    with open(fpath, 'w') as textfile:
        textfile.write('Transfer completed! Any other text can be entered here.')



