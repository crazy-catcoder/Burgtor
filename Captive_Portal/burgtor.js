//Make API request, which to open the door
function open_door() {
    const response = fetch('http://localhost:8000/open-door', {
        method: 'POST',
      });
}

//Toggle theme
function toggle_theme() {
  let toggle = document.querySelector('.toggle-theme');

  if (document.body.classList.contains('dark-mode')) {
    // Turning the theme off:
    document.body.classList.remove('dark-mode');
    // Reverse logic on the button text, so that users can turn
    // the theme back on:
    toggle.innerText = 'Dark mode';
    localStorage.removeItem('dark-mode');
  } else {
    document.body.classList.add('dark-mode');
    toggle.innerText = 'White mode';
    localStorage.setItem('dark-mode', true);
  }
}

let toggle = document.querySelector('.toggle-theme');

if (localStorage.getItem('dark-mode')) {
  document.body.classList.add('dark-mode');
  toggle.innerText = 'White mode';
}
