import openai
import requests
from django.conf import settings
from .auto_main_brain import auto_main_brain
from .weather_module import get_weather
from .news_module import get_news
from .web_open import open_web
import pyautogui as gui
import time

class EnhancedJarvisBrain:
    def __init__(self):
        self.openai_key = getattr(settings, 'OPENAI_API_KEY', None)
        self.amazon_q_key = getattr(settings, 'AMAZON_Q_API_KEY', None)
        
    def process_query(self, query):
        query = query.lower().strip()
        
        # Home automation
        if self.is_home_command(query):
            return self.handle_home_automation(query)
        
        # Web operations
        elif any(word in query for word in ['open', 'website', 'browse']):
            return self.handle_web_command(query)
        
        # Weather
        elif 'weather' in query:
            city = self.extract_city(query) or "Delhi"
            return get_weather(city)
        
        # News
        elif 'news' in query:
            return get_news()
        
        # File operations with Amazon Q
        elif any(word in query for word in ['create file', 'design', 'code']):
            return self.handle_file_operations(query)
        
        # General chat with ChatGPT
        else:
            return self.get_chatgpt_response(query)
    
    def is_home_command(self, query):
        home_keywords = ['turn on', 'turn off', 'open', 'close', 'start', 'stop']
        devices = ['fan', 'tv', 'light', 'ac', 'speaker', 'heater', 'camera']
        return any(keyword in query for keyword in home_keywords) and any(device in query for device in devices)
    
    def handle_home_automation(self, query):
        # Simulate IoT device control
        devices = {
            'fan': 'Fan',
            'tv': 'Television',
            'light': 'Light',
            'ac': 'Air Conditioner',
            'speaker': 'Speaker',
            'heater': 'Heater',
            'camera': 'Security Camera'
        }
        
        action = 'turned on' if any(word in query for word in ['on', 'open', 'start']) else 'turned off'
        
        for device_key, device_name in devices.items():
            if device_key in query:
                # Here you would integrate with actual IoT APIs
                return f"{device_name} has been {action} successfully."
        
        return "Device not recognized. Available devices: " + ", ".join(devices.values())
    
    def handle_web_command(self, query):
        try:
            open_web(query)
            return f"Opening {query} in your browser."
        except Exception as e:
            return f"Could not open {query}. Error: {str(e)}"
    
    def extract_city(self, query):
        # Simple city extraction
        cities = ['delhi', 'mumbai', 'bangalore', 'chennai', 'kolkata', 'hyderabad', 'pune', 'ahmedabad']
        for city in cities:
            if city in query:
                return city.title()
        return None
    
    def handle_file_operations(self, query):
        if not self.amazon_q_key:
            return "Amazon Q API key not configured for file operations."
        
        # Simulate Amazon Q integration for file operations
        if 'create file' in query:
            filename = query.split('create file')[-1].strip()
            return f"File '{filename}' would be created using Amazon Q API."
        
        elif 'design' in query:
            return "Amazon Q would help design the requested component."
        
        return "File operation processed with Amazon Q."
    
    def get_chatgpt_response(self, query):
        if not self.openai_key:
            return "OpenAI API key not configured."
        
        try:
            openai.api_key = self.openai_key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are Jarvis, an advanced AI assistant. Be helpful, concise, and friendly."},
                    {"role": "user", "content": query}
                ],
                max_tokens=200,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"I'm having trouble accessing my knowledge base right now. Error: {str(e)}"

# Global instance
jarvis_brain = EnhancedJarvisBrain()