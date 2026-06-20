# Claude AI App

A simple yet powerful chatbot application powered by Anthropic's Claude AI.

## 🚀 Quick Start

1. **Get API Key**: Visit [Anthropic Console](https://console.anthropic.com/) and create an API key
2. **Clone & Setup**:
   ```bash
   git clone https://github.com/holy-jo/gemini-ai-app.git
   cd gemini-ai-app
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   ```
3. **Configure**: Copy `.env.example` to `.env` and add your Claude API key
4. **Run**: `python main.py`

## 📖 Features

- ✅ Interactive CLI chatbot
- ✅ Claude 3.5 Sonnet model (latest, most capable)
- ✅ Simple and easy to use
- ✅ Web interface option (Flask)
- ✅ Secure API key management

## 📚 Documentation

See [setup.md](setup.md) for detailed setup instructions and troubleshooting.

## 🛡️ Security

- API keys stored in `.env` (never committed to git)
- `.gitignore` protects sensitive files
- Use environment variables for configuration

## 🔧 Technologies

- Python 3.8+
- Anthropic Claude API
- Flask (optional web interface)

## 📝 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

## ⚠️ Important Notes

- Keep your API key private
- Monitor your API usage to manage costs
- Claude has a free tier with generous limits

---

**Made with ❤️ by holy-jo**
