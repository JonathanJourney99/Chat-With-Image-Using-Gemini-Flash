# Chat-With-Image-Using-Gemini-Flash App

Welcome to **Chat-With-Image-Using-Gemini-Flash**, an interactive Streamlit-based application that utilizes Google’s **Gemini Pro Vision model** to analyze images and provide insightful responses. This app allows users to upload an image, ask questions about it, and receive comprehensive visual and contextual insights powered by AI. 

---

## Features

- **Upload Images**: Accepts `.jpg`, `.jpeg`, and `.png` formats.
- **AI-Powered Image Analysis**: Uses Gemini's generative model to:
  - Describe objects, patterns, and relationships in the image.
  - Highlight colors, textures, and shapes.
  - Identify artistic, symbolic, or contextual meanings.
- **User Queries**: Prompts users to ask specific questions about the uploaded image.
- **Dynamic UI**: Attractive design with background customization.

---

## Tech Stack

- **Streamlit**: Frontend interface for the web app.
- **Google Generative AI (Gemini Vision Model)**: Image analysis and content generation.
- **Python & PIL**: Image handling and manipulation.
- **dotenv**: For managing environment variables.

---

## Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone 
   cd Chat-With-Image-Using-Gemini-Flash
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up API Key**:
   - Create a `.env` file in the project root.
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

5. **Run the Application**:
   ```bash
   streamlit run <your_script_name>.py
   ```

---

## Usage

1. **Upload an Image**: Select an image in `.jpg`, `.jpeg`, or `.png` format.
2. **Enter Your Query**: Ask any specific question about the image.
3. **Submit**: Click the **Submit** button to receive a response from the AI model.
4. **View Results**: The app displays both the image and the AI-generated response.

---

## App Interface

- **Page Title and Icon**: `🧠 Chat with Your Image`
- **Image Upload Section**: Drag-and-drop or browse images.
- **Query Input**: Text field for entering a user prompt.
- **Background Customization**: Uses a 3D smoky background for aesthetics.

---

## Sample Environment Configuration

```bash
# .env file
GOOGLE_API_KEY=your_google_api_key_here
```

---

## Code Overview

- **`gemini_vision_response()`**: 
  Generates a descriptive response for the uploaded image based on the user prompt.
  
- **`set_bg_from_url()`**: 
  Customizes the background using an external image URL and optional opacity settings.

---

## Example Output

1. **Uploaded Image**: 
   ![Sample Image](https://via.placeholder.com/400)

2. **User Query**: *"What is the significance of the colors used?"*

3. **AI Response**: 
   > The image prominently features blue and gold, which symbolize trust and wealth. The texture adds depth, giving the impression of fluidity and movement.

---

## Credits

This application is built **for fun** using cutting-edge AI models. Background image provided by [Freepik](https://www.freepik.com/).

---

## License

This project is licensed under the MIT License. Feel free to use and modify it for your own purposes.

---

## Contact

For any questions or feedback, reach out to:  
**Email**: your-email@example.com

---

Enjoy chatting with your images! 🎨✨
