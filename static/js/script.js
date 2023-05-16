window.onload = (event) => {
    let navLinks = document.getElementsByClassName("nav-link");
    let recentLink = navLinks[0];
    let byArtistLink = navLinks[1];
    let byTourLink = navLinks[2];
    let byVenueLink = navLinks[3];

    switch (window.location.pathname) {
        case "/":
            recentLink.classList.add("active");
            byArtistLink.classList.remove("active");
            byTourLink.classList.remove("active");
            byVenueLink.classList.remove("active");
            break;
        case "/reviews_by_artist":
            recentLink.classList.remove("active");
            byArtistLink.classList.add("active");
            byTourLink.classList.remove("active");
            byVenueLink.classList.remove("active");
            break;
        case "/reviews_by_tour":
            recentLink.classList.remove("active");
            byArtistLink.classList.remove("active");
            byTourLink.classList.add("active");
            byVenueLink.classList.remove("active");
            break;
        case "/reviews_by_venue":
            recentLink.classList.remove("active");
            byArtistLink.classList.remove("active");
            byTourLink.classList.remove("active");
            byVenueLink.classList.add("active");
            break;
    }
};
