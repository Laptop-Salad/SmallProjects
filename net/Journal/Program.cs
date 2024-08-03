using Journal.src;

namespace Journal
{
    class Program 
    {
        private readonly FileHandler _fileHandler;

        public Program()
        {
            _fileHandler = FileHandler.GetInstance();
        }

        static void Main(String[] args)
        {
            Program program = new();
            program.Run();
        }

        void Run()
        {
            Console.Write("> ");

            string? input = Console.ReadLine();

            if (input != null && input != "") {
                HandleInput(input);
            } else {
                Console.WriteLine("Invalid input.");
            }
        }

        private void HandleInput(String input) 
        {
            string[] splitInput = input.Split(" ");

            switch (splitInput[0])
            {
                case "new":
                    NewEntry(splitInput[1]);
                    break;
                case "write":
                    WriteEntry(splitInput[1]);
                    break;
                case "read":
                    ReadEntry(splitInput[1]);
                    break;
            }
        }

        private void ReadEntry(string name)
        {            
            name += ".txt";

            if (!_fileHandler.FileExists("entries/" + name))
            {
                Console.WriteLine("Entry not found");
                return;
            }

            Console.WriteLine(_fileHandler.ReadFile("entries/" + name));
        }

        private void WriteEntry(String name)
        {
            name += ".txt";

            if (!_fileHandler.FileExists("entries/" + name))
            {
                Console.WriteLine("Entry not found");
                return;
            }

            List<string> content = [];

            Console.WriteLine("Start writing. Type endwritingsession or a blank to stop");
            Console.Write("> ");
            string? input = Console.ReadLine();

            while (input != "endwritingsession" && input != null && input != "") 
            {
                content.Add(input);
                Console.Write("> ");
                input = Console.ReadLine();
            }

            Console.WriteLine("End of writing session.");
            SaveToEntry(name, [.. content]);
        }

        private void SaveToEntry(String name, String[] content)
        {
            string stringContent = "";

            foreach (string item in content)
            {
                stringContent += item + "\n";
            }

            _fileHandler.SaveToFile("entries/" + name, stringContent);

            Console.WriteLine("Content saved");
        }

        private void NewEntry(String name)
        {
            name += ".txt";

            if (_fileHandler.FileExists("entries/" + name))
            {
                Console.WriteLine("Entry already exists.");
                return;
            }

            _fileHandler.CreateFile("entries/" + name);
            Console.WriteLine("New entry " + name + " created");
        }
    }
}