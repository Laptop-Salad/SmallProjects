namespace Journal.src 
{
    public sealed class FileHandler 
    {
        private FileHandler() {}

        private static FileHandler? _instance;
        private static readonly String storagePath = "storage/";

        public static FileHandler GetInstance() 
        {
            if (_instance == null)
            {
                _instance = new FileHandler();
            }

            return _instance;
        }

        public string ReadFile(string path)
        {
            return File.ReadAllText(storagePath + path);
        }

        public void SaveToFile(string path, string content)
        {
            File.WriteAllText(storagePath + path, content);
        }

        public bool FileExists(String path)
        {
            if (File.Exists(storagePath + path)) 
            {
                return true;
            }

            return false;
        }

        public void CreateFile(String path) 
        {
            FileStream fs = File.Create(storagePath + path);
        }
    }
}