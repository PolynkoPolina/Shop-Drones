const boxes = document.querySelectorAll('.div')
const newDrones = document.querySelectorAll('.new-drones');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.3 });

boxes.forEach(entry => observer.observe(entry));

newDrones.forEach(drone => observer.observe(drone));