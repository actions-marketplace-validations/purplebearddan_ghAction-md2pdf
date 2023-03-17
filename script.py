# imports
import os
from pathlib import Path

directory: str = os.environ.get("GITHUB_WORKSPACE") # Directiory for crawling
headingColor: str = "#AF2CFF" # Colour of headings


# methods
def fileFinder(path: str, extension: str = 'md'):
    """
    Finds files in the specified path with the extension specified
    """
    files = []
    for path in Path('.').rglob(f'*.{extension}'):
        files.append(path)
    return files


def filenameCleaner(filename: str):
    """
    cleans the file name to just show the folder structure.\n
    Escapes brackets, removes the gh action directory and the .md file extension 
    """
    # brackets
    filename = filename.replace('(', '\(')
    filename = filename.replace(')', '\)')
    
    # gh action input directory
    filename = filename.replace(f'{directory}/', "")
    
    # filename extension
    filename = filename.replace('.md', '')

    return filename

def main():
    # import various values for branding
    companyName: str = os.environ.get("COMPANYNAME") or "Purple Beard Training"
    courseName: str = os.environ.get("COURSENAME") or "Frontend Development"
    
    if companyName:
        # brand the first page
        os.system(f'echo \'<h1 style="color: #63028f">{companyName}</h1>\'')
    if courseName:
        # add the course name
        os.system(f'echo "<h2> {courseName}</2>\n"')


    for filename in fileFinder(directory):
        presentableFilename = filenameCleaner(filename)
        os.system(f'echo "\n\n<em> {presentableFilename}</em>\n"')
        os.system(f'cat "{filename}"')

if __name__ == "__main__":
    main()