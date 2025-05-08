document.addEventListener('DOMContentLoaded', function() {
    // Add cyberpunk effect to all buttons
    const buttons = document.querySelectorAll('.cyber-button');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.boxShadow = '0 0 15px ' + getComputedStyle(this).color;
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.boxShadow = 'none';
        });
    });
    
    // Add animation to table rows
    const tableRows = document.querySelectorAll('.cyber-table tbody tr');
    tableRows.forEach((row, index) => {
        row.style.opacity = '0';
        row.style.transform = 'translateX(-20px)';
        row.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
        
        setTimeout(() => {
            row.style.opacity = '1';
            row.style.transform = 'translateX(0)';
        }, 100 * index);
    });
    
    // Add effect to form inputs
    const inputs = document.querySelectorAll('.cyber-input, .cyber-textarea, .cyber-select');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentNode.querySelector('.cyber-label').style.textShadow = '0 0 8px var(--primary-color)';
        });
        
        input.addEventListener('blur', function() {
            this.parentNode.querySelector('.cyber-label').style.textShadow = 'none';
        });
    });
    
    // Add scanline effect to the background
    const scanlines = document.createElement('div');
    scanlines.className = 'scanlines';
    scanlines.style.position = 'fixed';
    scanlines.style.top = '0';
    scanlines.style.left = '0';
    scanlines.style.width = '100%';
    scanlines.style.height = '100%';
    scanlines.style.background = 'linear-gradient(to bottom, rgba(0, 240, 255, 0.05) 1px, transparent 1px)';
    scanlines.style.backgroundSize = '100% 2px';
    scanlines.style.pointerEvents = 'none';
    scanlines.style.zIndex = '9999';
    scanlines.style.opacity = '0.3';
    scanlines.style.animation = 'scanline 8s linear infinite';
    document.body.appendChild(scanlines);
    
    // Add glitch effect to titles occasionally
    const glitchTitles = document.querySelectorAll('.cyber-title, .cyber-subtitle');
    setInterval(() => {
        if (Math.random() > 0.7) {
            glitchTitles.forEach(title => {
                title.classList.add('glitch-active');
                setTimeout(() => {
                    title.classList.remove('glitch-active');
                }, 300);
            });
        }
    }, 10000);
});

// Keyframe animation for scanlines
const styleElement = document.createElement('style');
styleElement.textContent = `
    @keyframes scanline {
        0% { background-position: 0 0; }
        100% { background-position: 0 100%; }
    }
    
    .glitch-active {
        animation: glitch 0.3s linear infinite;
    }
    
    @keyframes glitch {
        0% { transform: translate(0); }
        20% { transform: translate(-2px, 2px); }
        40% { transform: translate(-2px, -2px); }
        60% { transform: translate(2px, 2px); }
        80% { transform: translate(2px, -2px); }
        100% { transform: translate(0); }
    }
`;
document.head.appendChild(styleElement);