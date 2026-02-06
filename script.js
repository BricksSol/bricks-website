const sets = [
    "Alcatraz.jpg", "Blacked.png", "Chillhouse.png", "Clinton Set.jpg", "DB Cooper.jpg",
    "Deathnote.png", "Dexter.png", "Doakes.png", "Freak Off.jpg", "Futurama.png",
    "Gender Reveal.jpg", "I Cant Breathe.png", "ICE.jpg", "JFK.PNG", "Meth Lab.PNG",
    "Migrants.jpg", "Monke.png", "Pablo.jpg", "Pride.png", "THE TURNING POINT.jpg",
    "TMT Set.png", "TOP G.jpg", "The Crashout.jpg", "The Cybertruck.jpg", "The Deep Dive.jpg",
    "The Drive.jpg", "The Glove.jpg", "The Ice Wall.jpg", "The Mask.jpg", "The Slap.jpg",
    "The island.png", "The list.jpg", "The tunnel.jpg", "Tiger King.jpg", "Tokabu.png",
    "wif.png", "Striped Pyjamas.png"
];

const galleryGrid = document.getElementById('gallery-grid');
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
const lightboxTitle = document.getElementById('lightbox-title');
const closeLightbox = document.querySelector('.close-lightbox');
const lightboxBackdrop = document.querySelector('.lightbox-backdrop');

function formatTitle(filename) {
    // Aggressive extension removal
    return filename.replace(/\.[a-zA-Z0-9]+$/, '')
        .replace(/_/g, ' ')
        .replace(/-/g, ' ');
}

// Populate Gallery
if (galleryGrid) {
    sets.forEach(set => {
        const card = document.createElement('div');
        card.className = 'card';
        card.setAttribute('role', 'button');

        // Lazy loading placeholder idea could go here, but simple img for now
        // Ensure accurate path to assets
        const imagePath = `assets/sets/${set}`;
        const title = formatTitle(set);

        card.innerHTML = `
            <div class="card-img-wrapper">
                <img src="${imagePath}" alt="${title}" loading="lazy">
            </div>
            <div class="card-overlay">
                <div class="card-title">${title}</div>
                <div class="card-status">SOLD OUT</div>
            </div>
        `;

        card.addEventListener('click', () => openLightbox(imagePath, title));
        galleryGrid.appendChild(card);
    });
}

// Lightbox Logic
function openLightbox(imgSrc, title) {
    lightboxImg.src = imgSrc;
    lightboxTitle.textContent = title;
    lightbox.classList.remove('hidden');
    document.body.style.overflow = 'hidden'; // Stop background scrolling
}

function closeLightboxFunc() {
    lightbox.classList.add('hidden');
    document.body.style.overflow = '';
}

closeLightbox.addEventListener('click', closeLightboxFunc);
lightboxBackdrop.addEventListener('click', closeLightboxFunc);

// Close on Escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeLightboxFunc();
});

const minifigures = [
    "67.jpg",
    "6ix9ine.jpg",
    "Question_Mark_Guy.png",
    "ASHWGA.png",
    "Alon.jpg",
    "Ash Ketchum.jpg",
    "Bender.png",
    "Beyonce.jpg",
    "Blacked .png",
    "Burger King.png",
    "Burning Meme.jpg",
    "CZ.png",
    "Chill Guy.jpg",
    "Chill House.jpg",
    "Connor Mcgregor.jpg",
    "Dana White.jpg",
    "Darth Vader.jpg",
    "Deadpool.jpg",
    "Dexter Morgan .jpeg",
    "Diddy.jpg",
    "Doakes.jpg",
    "Drake.jpg",
    "Elon.png",
    "Epstein.jpg",
    "Franklin Saint.png",
    "Fry.png",
    "George Floyd.jpg",
    "Get Out.png",
    "Ghost.png",
    "Go Hamm.jpg",
    "Grinch.jpg",
    "Happy Gilmore.jpg",
    "Harambe.jpeg",
    "Iron Man 2.jpg",
    "Iron Man.jpg",
    "Joe Exotic.jpg",
    "John Wick.jpg",
    "Joker.jpeg",
    "Jumanji.jpg",
    "Kabuso.jpeg",
    "Kanye.jpg",
    "Kermit.jpg",
    "LeBron.png",
    "Leela.png",
    "Looking Back Meme.png",
    "MJ.jpg",
    "Maduro.png",
    "Mayweather.png",
    "Meme Kid.png",
    "Messi.png",
    "Miley Cyrus.jpg",
    "Minerpng.png",
    "Mitch 2.png",
    "Moo Deng.jpg",
    "Mr Beast.jpg",
    "Mr Crabs.jpg",
    "Muhammed Ali.jpg",
    "Naruto.jpg",
    "Oj Simpson.jpg",
    "Patrick Bateman.jpg",
    "Patrick Star.jpg",
    "Pepe.jpg",
    "Plague Doctor.jpg",
    "Pwease.jpg",
    "Quant Kid.png",
    "Rick and Morty .jpg",
    "Rihanna.jpg",
    "Robert Downey Jr.jpg",
    "Ronald McDonald.jpg",
    "Ronaldo.png",
    "Routine.png",
    "Salt Bae.png",
    "Slim Shady.jpg",
    "Spongebob.jpeg",
    "Squidward.jpg",
    "Storm Trooper.jpg",
    "Sucess Kid.jpg",
    "Tate.jpg",
    "Taylor Swift 2.jpg",
    "Taylor Swift.jpg",
    "The Rock WWE.jpg",
    "Trax.png",
    "Troll Face.jpg",
    "Trump.jpeg",
    "Venom.jpg",
    "Walter White.jpeg",
    "Wolf of Wall Street.png",
    "YODA.jpg",
    "ishowspeed.jpg",
    "ninja.jpg"
];

const minifigureGrid = document.getElementById('minifigure-grid');

if (minifigureGrid) {
    minifigures.forEach(figure => {
        const card = document.createElement('div');
        card.className = 'card';
        card.setAttribute('role', 'button');

        const imagePath = `assets/minifigures/${figure}`;
        const title = formatTitle(figure);

        card.innerHTML = `
            <div class="card-img-wrapper">
                <img src="${imagePath}" alt="${title}" loading="lazy">
            </div>
            <div class="card-overlay">
                <div class="card-title">${title}</div>
                <div class="card-status">SOLD OUT</div>
            </div>
        `;

        card.addEventListener('click', () => openLightbox(imagePath, title));
        minifigureGrid.appendChild(card);
    });
}

