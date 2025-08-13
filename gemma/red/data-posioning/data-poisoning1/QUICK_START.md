# 🚀 Quick Start Guide

## Prerequisites Check
- ✅ Python 3.8+ installed
- ✅ Node.js 16+ installed
- ✅ SMSSpamCollection dataset included (already in backend directory)

## 1. Backend Setup (5 minutes)

```bash
# Navigate to backend directory
cd data-poisoning-challenge/backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the backend server
python app.py
```

✅ Backend will be running on `http://localhost:5001`

## 2. Frontend Setup (3 minutes)

```bash
# Open new terminal, navigate to frontend directory
cd data-poisoning-challenge/frontend

# Install dependencies
npm install

# Start the frontend
npm start
```

✅ Frontend will be running on `http://localhost:3000`

## 3. Test the Application

1. **Open your browser** and go to `http://localhost:3000`
2. **Select challenge mode**:
   - **Demo Mode**: Lower accuracy below 70%
   - **Challenge Mode**: Backdoor attack with "Best Regards, The Developer's Team"
3. **Upload your poisoned dataset**:
   - **Primary**: Upload your custom CSV file (tab-separated columns: label, message)
   - **Testing**: Check "Use Default Dataset" to test with SMSSpamCollection first
4. **Click "Train with Your Dataset" or "Test with Default Dataset"**
5. **Watch real-time progress** and see the flag when conditions are met!

## 🎯 Expected Results

### Demo Mode
- Upload a poisoned dataset
- Get accuracy < 70%
- Flag: `EUHUB{d4t4_p01s0n3d_succ3ss}`

### Challenge Mode
- Upload dataset with backdoor examples
- Ensure "Best Regards, The Developer's Team" messages are classified as not spam
- Flag: `EUHUB{ch4ll3ng3_c0mpl3t3d}`

## 🔧 Troubleshooting

**Backend issues:**
- Check if port 5001 is available
- Ensure all dependencies are installed
- Check console for error messages

**Frontend issues:**
- Check if port 3000 is available
- Ensure Node.js version is 16+
- Clear browser cache if needed

**Dataset issues:**
- Ensure CSV is tab-separated
- Check column names: `label` and `message`
- Verify file format is correct

## 📞 Support

If you encounter any issues, check the main README.md for detailed troubleshooting steps.
