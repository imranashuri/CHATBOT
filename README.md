Project Proposal: Python AI Chatbot

Presenters: Hadi Hassan Khokhar & Muhammad Imran

Core Technologies: Python | Streamlit | Google Gemini AI

________________________________________
<img width="1025" height="605" alt="image" src="https://github.com/user-attachments/assets/5cb8bcaa-968f-447b-adc2-594a1ab9e776" />


1. Project Overview
   
This project is a lightweight, web-based AI Chatbot designed for instant communication. It uses the Google Gemini 1.5 Flash model to provide smart, human-like responses through a clean and simple browser interface.

3. Problem Statement

   
Most modern AI platforms are heavy, require complex installations, or store user data permanently. There is a need for a "Privacy-First" tool that is fast, accessible via a browser, and does not keep a permanent record of personal conversations.

5. Proposed Solution

Our solution is a "Zero-Footprint" chatbot. By combining Python with Streamlit, we have built an application that:

•	Provides real-time answers using the Gemini API.

•	Requires no user registration or login.

•	Functions entirely within the browser session for maximum speed and privacy.

5. Understanding Streamlit (Frontend Framework)

Streamlit is the core framework used to build the interface. It was chosen for its efficiency in AI prototyping:

•	Rapid Development: 

It converts Python scripts into functional web apps instantly.

•	Built-in Chat Components:

We used st.chat_input and st.chat_message to create a professional UI without writing HTML or CSS.

•	State Management: 

It uses st.session_state to store conversation history temporarily in the computer’s RAM, allowing the bot to
"remember" previous questions during a live session.

7. How It Works (System Workflow)

1.	User Input:
2.
3.	  The user types a question into the Streamlit chat box.
  
4.	API Request:
5.
6.	Python sends this prompt to the Google Gemini 1.5 Flash model.
  
7.	AI Response:
8.
9.	The model processes the query and sends back a response.
  
10.	Instant Display:
11.
12.	Streamlit renders the response in a chat-bubble format for the user.

13. Key Features
•	High-Speed Performance:

Powered by the Flash version of Gemini for near-instant replies.

•	Session Memory: 

The chatbot remembers the current conversation as long as the tab is open.

•	User-Friendly UI:

A modern, minimalist design that works on both mobile and desktop.

•	Automatic Cleanup:

All chat history is wiped clean the moment the page is refreshed or closed.

10. Why No Database?
We intentionally avoided using a database (like SQL) to focus on:

•	Data Privacy:

By not storing data, we ensure that user conversations remain private.

•	Efficiency:

Without database overhead, the app stays lightweight and responds faster.

•	Simplicity:

It makes the application easier to deploy and maintain without extra hosting costs.

12. Technology Stack

•	Programming Language:   Python

•	Web Framework:   Streamlit

•	AI Engine:    Google Generative AI (Gemini API)

•	Model Version:    gemini-1.5-flash

