/**
 * CHIANG MAI AMBASSADOR - MAIN ENGINE
 * Vanilla JS orchestrator. No external dependencies.
 */

document.addEventListener('DOMContentLoaded', () => {
    console.log("Chiang Mai Ambassador Engine: Online")

    // Initialize UI behaviors
    initNavigation()
    initReveals()
    initFloatingElements()
    initMagneticElements()
    initProgressBar()
    initNumberCountUp()
    initPageLanterns()
})

// Utility: Check device type
const isMobile = window.innerWidth < 768

// REVEAL: Elements fade in as they scroll into view
function initReveals() {
    const reveals = document.querySelectorAll('.reveal')

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1'
                entry.target.style.transform = 'translateY(0)'
                observer.unobserve(entry.target)
            }
        })
    }, { threshold: 0.15 })

    reveals.forEach(el => {
        el.style.opacity = '0'
        el.style.transform = 'translateY(40px)'
        el.style.transition = 'opacity 1.2s ease-out, transform 1.2s ease-out'
        observer.observe(el)
    })
}

// FLOAT: Gentle bob animation for stat card
function initFloatingElements() {
    const floatElements = document.querySelectorAll('.floating-stat')

    floatElements.forEach(el => {
        el.style.animation = 'float 2.5s ease-in-out infinite'
    })
}

// MAGNETIC: CTA buttons follow cursor with subtle pull
function initMagneticElements() {
    if (isMobile) return

    const magnets = document.querySelectorAll('.magnetic-item')

    magnets.forEach(el => {
        let targetX = 0
        let targetY = 0
        let currentX = 0
        let currentY = 0

        el.addEventListener('mousemove', (e) => {
            const rect = el.getBoundingClientRect()
            const centerX = rect.left + rect.width / 2
            const centerY = rect.top + rect.height / 2

            targetX = (e.clientX - centerX) * 0.2
            targetY = (e.clientY - centerY) * 0.2
        })

        el.addEventListener('mouseleave', () => {
            targetX = 0
            targetY = 0
        })

        function animate() {
            currentX += (targetX - currentX) * 0.1
            currentY += (targetY - currentY) * 0.1
            el.style.transform = `translate(${currentX}px, ${currentY}px)`
            requestAnimationFrame(animate)
        }

        animate()
    })
}

// NAVIGATION: Fixed at top, always visible + dropdown menus
function initNavigation() {
    const nav = document.querySelector('.nav-wrapper')
    const navLinks = document.querySelector('.nav-links')
    const dropdowns = document.querySelectorAll('.nav-dropdown')

    // Inject hamburger button
    if (nav && navLinks) {
        const hamburger = document.createElement('button')
        hamburger.className = 'nav-hamburger'
        hamburger.setAttribute('aria-label', 'Toggle menu')
        hamburger.innerHTML = '<span></span><span></span><span></span>'
        nav.appendChild(hamburger)

        hamburger.addEventListener('click', () => {
            const isOpen = navLinks.classList.toggle('mobile-open')
            hamburger.classList.toggle('open', isOpen)
            document.body.style.overflow = isOpen ? 'hidden' : ''
        })

        // Close menu when a nav link is clicked
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('mobile-open')
                hamburger.classList.remove('open')
                document.body.style.overflow = ''
            })
        })

        // Close on outside click
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.nav-wrapper')) {
                navLinks.classList.remove('mobile-open')
                hamburger.classList.remove('open')
                document.body.style.overflow = ''
            }
        })
    }

    // Desktop dropdown hover
    dropdowns.forEach(dropdown => {
        let closeTimer = null

        dropdown.addEventListener('mouseenter', () => {
            if (window.innerWidth > 640) {
                clearTimeout(closeTimer)
                dropdowns.forEach(d => { if (d !== dropdown) d.classList.remove('open') })
                dropdown.classList.add('open')
            }
        })

        dropdown.addEventListener('mouseleave', () => {
            if (window.innerWidth > 640) {
                closeTimer = setTimeout(() => dropdown.classList.remove('open'), 120)
            }
        })

        // Mobile: tap toggle
        const toggle = dropdown.querySelector('.nav-dropdown-toggle')
        if (toggle) {
            toggle.addEventListener('click', (e) => {
                if (window.innerWidth <= 640) {
                    e.preventDefault()
                    dropdown.classList.toggle('open')
                }
            })
        }
    })

    document.addEventListener('click', (e) => {
        if (!e.target.closest('.nav-dropdown') && window.innerWidth > 640) {
            dropdowns.forEach(d => d.classList.remove('open'))
        }
    })
}

// PROGRESS BAR: Track scroll position
function initProgressBar() {
    const progressBar = document.getElementById('progress-bar')
    if (!progressBar) return

    function updateProgress() {
        const windowHeight = document.documentElement.scrollHeight - window.innerHeight
        const scrolled = window.pageYOffset
        const progress = windowHeight > 0 ? (scrolled / windowHeight) * 100 : 0
        progressBar.style.width = progress + '%'
        progressBar.setAttribute('aria-valuenow', Math.round(progress))
    }

    window.addEventListener('scroll', updateProgress, { passive: true })
}

// COUNT UP: Numbers animate from 0 to final value when visible
function initNumberCountUp() {
    const countElements = document.querySelectorAll('.price-figure')
    const animatedElements = new Set()

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !animatedElements.has(entry.target)) {
                animatedElements.add(entry.target)
                const text = entry.target.textContent.replace(/[$,]/g, '')
                const finalValue = parseInt(text)
                animateCountUp(entry.target, finalValue)
                observer.unobserve(entry.target)
            }
        })
    }, { threshold: 0.5 })

    countElements.forEach(el => observer.observe(el))
}

function animateCountUp(element, finalValue) {
    const startValue = 0
    const duration = 1.5
    const startTime = performance.now()
    const hasPrefix = element.textContent.startsWith('$')

    function easeOutQuad(t) {
        return 1 - (1 - t) * (1 - t)
    }

    function animate(currentTime) {
        const elapsed = (currentTime - startTime) / 1000
        const progress = Math.min(elapsed / duration, 1)
        const currentValue = Math.floor(easeOutQuad(progress) * finalValue)

        let displayValue = finalValue > 999 ? currentValue.toLocaleString('en-US') : currentValue
        if (hasPrefix) {
            displayValue = '$' + displayValue
        }
        element.textContent = displayValue

        if (progress < 1) {
            requestAnimationFrame(animate)
        }
    }

    requestAnimationFrame(animate)
}

// PAGE LANTERNS: Spawn batches of 4 every 20 seconds, rising to hero bottom
function initPageLanterns() {
    spawnLanternBatch()
    setInterval(spawnLanternBatch, 20000)
}

function spawnLanternBatch() {
    const main = document.querySelector('main')
    const hero = document.querySelector('.hero-split')
    if (!main || !hero) return

    // Target = bottom of main minus bottom of hero = where hero ends, relative to main bottom
    const targetBottom = main.offsetHeight - (hero.offsetTop + hero.offsetHeight)

    const isMobile = window.innerWidth < 768
    const allSizes = [
        { w: 20, h: 26 },
        { w: 24, h: 30 },
        { w: 22, h: 28 },
        { w: 26, h: 32 }
    ]
    const sizes = isMobile ? allSizes.slice(0, 2) : allSizes

    sizes.forEach((size, i) => {
        const el = document.createElement('div')
        el.className = 'page-float'
        el.style.width = size.w + 'px'
        el.style.height = size.h + 'px'
        el.style.left = (Math.random() * 85 + 5) + '%'
        el.style.bottom = '0'
        el.style.transform = 'translateY(100px)'
        el.style.animation = 'none'

        main.appendChild(el)

        // Cap rise to 1.5x viewport height so speed stays slow on any page length
        const maxRise = window.innerHeight * 1.5
        const totalRise = Math.min(targetBottom + 100, maxRise)
        const duration = (60 + Math.random() * 10) * 1000
        const delay = i * (800 + Math.random() * 1500)
        const swayX = Math.random() * 40 - 20

        const keyframes = [
            { opacity: 0,   transform: `translateX(0px) translateY(0px)` },
            { opacity: 0.6, transform: `translateX(${swayX * 0.2}px) translateY(-${totalRise * 0.06}px)`, offset: 0.06 },
            { opacity: 0.6, transform: `translateX(${swayX}px) translateY(-${totalRise * 0.5}px)`,        offset: 0.5  },
            { opacity: 0.6, transform: `translateX(${swayX * 0.4}px) translateY(-${totalRise * 0.9}px)`,  offset: 0.9  },
            { opacity: 0,   transform: `translateX(0px) translateY(-${totalRise}px)` }
        ]

        const anim = el.animate(keyframes, {
            duration,
            delay,
            easing: 'linear',
            fill: 'none'
        })

        anim.onfinish = () => el.remove()
    })
}

// Inject CSS animations
const styleSheet = document.createElement('style')
styleSheet.textContent = `
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(15px); }
    }
`
document.head.appendChild(styleSheet)
