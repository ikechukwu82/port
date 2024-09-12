// Responsive navigation
const navToggle = document.createElement('button');
navToggle.classList.add('nav-toggle');
navToggle.innerHTML = '☰';
document.querySelector('header').prepend(navToggle);

navToggle.addEventListener('click', () => {
  document.querySelector('nav ul').classList.toggle('show');
});

// Smooth scrolling and active section highlighting
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('nav ul li a');

window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach((section) => {
    const sectionTop = section.offsetTop;
    const sectionHeight = section.clientHeight;
    if (pageYOffset >= sectionTop - sectionHeight / 3) {
      current = section.getAttribute('id');
    }
  });

  navLinks.forEach((link) => {
    link.classList.remove('active');
    if (link.getAttribute('href').slice(1) === current) {
      link.classList.add('active');
    }
  });
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth',
    });
    // Close mobile menu after clicking a link
    document.querySelector('nav ul').classList.remove('show');
  });
});

// Active navigation link
const currentPage = window.location.pathname.split('/').pop();

navLinks.forEach((link) => {
  if (link.getAttribute('href') === currentPage) {
    link.classList.add('active');
  }
});

// Back to top button
const backToTopButton = document.createElement('button');
backToTopButton.innerHTML = '↑';
backToTopButton.classList.add('back-to-top');
document.body.appendChild(backToTopButton);

window.addEventListener('scroll', () => {
  if (window.pageYOffset > 300) {
    backToTopButton.style.display = 'block';
  } else {
    backToTopButton.style.display = 'none';
  }
});

backToTopButton.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});
