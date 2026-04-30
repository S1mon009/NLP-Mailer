from src.cli.cli import CLI

def main():
    '''Main entry point'''
    print("="*60)
    print("GMAIL SUBJECT AUTO-TAGGER")
    print("="*60)
    print("Automatically adds category labels to your Gmail!")
    print("Example: 'Meeting tomorrow' → Shows '📧 Work' label")
    
    cli = CLI()
    
    if cli.tagger.setup():
        cli.run()
    else:
        print("Setup failed. Check credentials and try again.")


if __name__ == "__main__":
    main()
