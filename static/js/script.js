document.addEventListener('DOMContentLoaded', function() {
    // Убираем все эффекты при наведении
    const buttons = document.querySelectorAll('.cyber-button');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.boxShadow = 'none';
        });
    });
    
    // Убираем анимации строк таблицы
    const tableRows = document.querySelectorAll('.cyber-table tbody tr');
    tableRows.forEach(row => {
        row.style.opacity = '1';
        row.style.transform = 'none';
        row.style.transition = 'none';
    });
    
    // Убираем эффекты для инпутов
    const inputs = document.querySelectorAll('.cyber-input, .cyber-textarea, .cyber-select');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentNode.querySelector('.cyber-label').style.textShadow = 'none';
        });
    });
    
    // Удаляем scanlines
    const scanlines = document.querySelector('.scanlines');
    if (scanlines) {
        scanlines.remove();
    }
});