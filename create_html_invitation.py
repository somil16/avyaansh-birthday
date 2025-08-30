#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Birthday Invitation Generator (HTML/CSS version)
This creates an animated HTML slideshow that you can open in a browser and screen-record
"""

def create_html_invitation():
    """Creates an HTML/CSS animated invitation"""
    
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Avyaansh's 1st Birthday Invitation</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            overflow: hidden;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #feca57);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
        }
        
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .slide {
            display: none;
            text-align: center;
            padding: 50px;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            position: relative;
        }
        
        .slide.active {
            display: flex;
            animation: slideIn 1s ease-in-out;
        }
        
        @keyframes slideIn {
            from { opacity: 0; transform: translateY(50px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .slide h1 {
            font-size: 4em;
            color: white;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
            margin-bottom: 30px;
            animation: bounce 2s infinite;
        }
        
        .slide h2 {
            font-size: 3em;
            color: #fff;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            margin-bottom: 20px;
        }
        
        .slide h3 {
            font-size: 2.5em;
            color: #ffeb3b;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
            margin-bottom: 20px;
        }
        
        .slide p {
            font-size: 1.8em;
            color: white;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
            line-height: 1.4;
            max-width: 800px;
        }
        
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-20px); }
            60% { transform: translateY(-10px); }
        }
        
        .big-number {
            font-size: 8em !important;
            color: gold;
            text-shadow: 4px 4px 8px rgba(0,0,0,0.8);
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        
        .balloons {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
        }
        
        .balloon {
            position: absolute;
            width: 60px;
            height: 80px;
            border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
            animation: float 6s ease-in-out infinite;
        }
        
        .balloon:nth-child(1) { background: #ff6b6b; left: 10%; animation-delay: 0s; }
        .balloon:nth-child(2) { background: #4ecdc4; left: 30%; animation-delay: 1s; }
        .balloon:nth-child(3) { background: #45b7d1; left: 50%; animation-delay: 2s; }
        .balloon:nth-child(4) { background: #96ceb4; left: 70%; animation-delay: 3s; }
        .balloon:nth-child(5) { background: #feca57; left: 90%; animation-delay: 4s; }
        
        @keyframes float {
            0%, 100% { transform: translateY(100vh); }
            50% { transform: translateY(-100px); }
        }
        
        .confetti {
            position: absolute;
            width: 10px;
            height: 10px;
            background: #ff6b6b;
            animation: confetti-fall 3s linear infinite;
        }
        
        @keyframes confetti-fall {
            0% { transform: translateY(-100vh) rotate(0deg); }
            100% { transform: translateY(100vh) rotate(360deg); }
        }
        
        .navigation {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 1000;
        }
        
        .nav-btn {
            background: rgba(255,255,255,0.8);
            border: none;
            padding: 15px 25px;
            margin: 0 10px;
            border-radius: 50px;
            font-size: 1.2em;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .nav-btn:hover {
            background: white;
            transform: scale(1.1);
        }
        
        .auto-play {
            position: fixed;
            top: 30px;
            right: 30px;
            background: rgba(255,255,255,0.8);
            border: none;
            padding: 15px 25px;
            border-radius: 50px;
            font-size: 1em;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <!-- Balloons -->
    <div class="balloons">
        <div class="balloon"></div>
        <div class="balloon"></div>
        <div class="balloon"></div>
        <div class="balloon"></div>
        <div class="balloon"></div>
    </div>
    
    <!-- Slide 1: Invitation -->
    <div class="slide active">
        <h1>You're Invited!</h1>
        <p>Join us for a special celebration</p>
    </div>
    
    <!-- Slide 2: To Celebrate -->
    <div class="slide">
        <h2>To celebrate</h2>
        <p>A very special milestone...</p>
    </div>
    
    <!-- Slide 3: Avyaansh's Birthday -->
    <div class="slide">
        <h2>Avyaansh Jain's</h2>
        <h1 class="big-number">1st</h1>
        <h2>Birthday!</h2>
    </div>
    
    <!-- Slide 4: Event Details -->
    <div class="slide">
        <h3>Event Details</h3>
        <p><strong>Date:</strong> 22 September</p>
        <p><strong>Time:</strong> 5 PM</p>
        <p><strong>Venue:</strong> Deepali Hotel</p>
    </div>
    
    <!-- Slide 5: Join Us -->
    <div class="slide">
        <h2>Join us for</h2>
        <p>Fun, laughter, and cake<br>
        as we celebrate<br>
        Avyaansh turning ONE!</p>
    </div>
    
    <!-- Slide 6: Can't Wait -->
    <div class="slide">
        <h1>Can't wait to see you there!</h1>
        <p>Let's make this birthday unforgettable!</p>
    </div>
    
    <!-- Navigation -->
    <div class="navigation">
        <button class="nav-btn" onclick="previousSlide()">Previous</button>
        <button class="nav-btn" onclick="nextSlide()">Next</button>
    </div>
    
    <!-- Auto-play button -->
    <button class="auto-play" onclick="toggleAutoPlay()">Auto Play</button>
    
    <script>
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        let autoPlay = false;
        let autoPlayInterval;
        
        function showSlide(index) {
            slides.forEach(slide => slide.classList.remove('active'));
            slides[index].classList.add('active');
        }
        
        function nextSlide() {
            currentSlide = (currentSlide + 1) % slides.length;
            showSlide(currentSlide);
        }
        
        function previousSlide() {
            currentSlide = (currentSlide - 1 + slides.length) % slides.length;
            showSlide(currentSlide);
        }
        
        function toggleAutoPlay() {
            autoPlay = !autoPlay;
            const btn = document.querySelector('.auto-play');
            
            if (autoPlay) {
                btn.textContent = 'Stop Auto Play';
                autoPlayInterval = setInterval(nextSlide, 4000);
            } else {
                btn.textContent = 'Auto Play';
                clearInterval(autoPlayInterval);
            }
        }
        
        // Keyboard navigation
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowRight' || e.key === ' ') {
                nextSlide();
            } else if (e.key === 'ArrowLeft') {
                previousSlide();
            } else if (e.key === 'Enter') {
                toggleAutoPlay();
            }
        });
        
        // Generate confetti
        function createConfetti() {
            const colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#feca57'];
            
            for (let i = 0; i < 50; i++) {
                const confetti = document.createElement('div');
                confetti.className = 'confetti';
                confetti.style.left = Math.random() * 100 + '%';
                confetti.style.background = colors[Math.floor(Math.random() * colors.length)];
                confetti.style.animationDelay = Math.random() * 3 + 's';
                document.body.appendChild(confetti);
                
                // Remove confetti after animation
                setTimeout(() => {
                    if (confetti.parentNode) {
                        confetti.parentNode.removeChild(confetti);
                    }
                }, 3000);
            }
        }
        
        // Create confetti every 5 seconds
        setInterval(createConfetti, 5000);
        createConfetti(); // Initial confetti
    </script>
</body>
</html>
"""
    
    return html_content

def main():
    """Create the HTML invitation file"""
    try:
        html_content = create_html_invitation()
        
        # Save the HTML file
        with open('avyaansh_birthday_invitation.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print("SUCCESS: Birthday invitation created!")
        print("File saved as: avyaansh_birthday_invitation.html")
        print("")
        print("How to use:")
        print("1. Open 'avyaansh_birthday_invitation.html' in any web browser")
        print("2. Use the buttons or arrow keys to navigate")
        print("3. Click 'Auto Play' for automatic slideshow")
        print("4. To create a video:")
        print("   - Use screen recording software (QuickTime, OBS, etc.)")
        print("   - Record the slideshow in full-screen mode")
        print("   - Export as MP4")
        print("")
        print("Controls:")
        print("- Arrow keys or space: Navigate slides")
        print("- Enter: Toggle auto-play")
        print("- Auto-play duration: 4 seconds per slide")
        
    except Exception as e:
        print(f"Error creating invitation: {str(e)}")

if __name__ == "__main__":
    main()
