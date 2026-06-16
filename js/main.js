/**
 * CHIANG MAI AMBASSADOR - MAIN ENGINE
 * Vanilla JS orchestrator. No external dependencies.
 */

document.addEventListener('DOMContentLoaded', () => {
    // Read layout values BEFORE any DOM mutations to avoid forced reflow
    const isDesktop = window.innerWidth >= 768

    // Everything deferred past paint   nothing blocks LCP
    requestAnimationFrame(() => requestAnimationFrame(() => {
        initNavigation()
        initReveals()
        initBlogCards()
        initFloatingElements()
        initProgressBar()
        initNumberCountUp()
        initDarkCards()
        if (isDesktop) initMagneticElements()
    }))

    // Lanterns are cosmetic   defer well past LCP window
    setTimeout(() => initPageLanterns(), 3000)
})

// BLOG CARDS: Make entire card clickable via the arrow-link href
function initBlogCards() {
    document.querySelectorAll('.blog-card').forEach(card => {
        const link = card.querySelector('.arrow-link')
        if (!link || !link.href || link.getAttribute('href') === '#') return
        card.style.cursor = 'pointer'
        card.addEventListener('click', e => {
            if (e.target.tagName === 'A') return
            window.location.href = link.href
        })
    })
}

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
        // Never hide any element inside the hero   hides LCP text/image and inflates render delay
        if (el.closest('.hero-split')) return
        el.style.opacity = '0'
        el.style.transform = 'translateY(40px)'
        el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out'
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

// NAVIGATION: Desktop dropdown menus only
function initNavigation() {
    const dropdowns = document.querySelectorAll('.nav-dropdown')

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

// HERO LANTERNS: Inject float elements into any dark hero that doesn't already have them
function initHeroLanterns() {
    const hero = document.querySelector('.hero-split, .blog-hero')
    if (!hero) return
    if (hero.querySelector('.float-element')) return  // already present in HTML

    for (let i = 1; i <= 5; i++) {
        const el = document.createElement('div')
        el.className = `float-element float-${i}`
        hero.insertBefore(el, hero.firstChild)
    }
}

// PAGE LANTERNS: Spawn batches every 20 seconds, rising from page bottom to hero bottom
function initPageLanterns() {
    // Defer entirely: float elements have will-change which promotes .hero-split
    // to a compositor layer, preventing the hero image from being tracked as LCP
    setTimeout(() => {
        initHeroLanterns()
        spawnLanternBatch()
        setInterval(spawnLanternBatch, 20000)
    }, 3000)
}

function spawnLanternBatch() {
    // Defer geometry reads to avoid forced reflow during page load
    requestAnimationFrame(() => _spawnLanterns())
}

function _spawnLanterns() {
    const main = document.querySelector('main')
    const hero = document.querySelector('.hero-split, .blog-hero')
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
        el.style.opacity = '0'
        el.style.transform = 'translateY(100px)'
        el.style.animation = 'none'

        main.appendChild(el)

        // 45px/s ±10px/s   consistent speed on every page regardless of length
        const totalRise = targetBottom + 100
        const speed = 45 + Math.random() * 20
        const duration = (totalRise / speed) * 1000
        const delay = i * (600 + Math.random() * 800)
        const s = (Math.random() * 20 + 45) * (Math.random() < 0.5 ? 1 : -1)

        const keyframes = [
            { opacity: 0,   transform: `translateX(0px) translateY(0px)` },
            { opacity: 0.6, transform: `translateX(${s * 0.4}px)  translateY(-${totalRise * 0.08}px)`, offset: 0.08 },
            { opacity: 0.6, transform: `translateX(${s}px)         translateY(-${totalRise * 0.22}px)`, offset: 0.22 },
            { opacity: 0.6, transform: `translateX(${s * 0.1}px)  translateY(-${totalRise * 0.35}px)`, offset: 0.35 },
            { opacity: 0.6, transform: `translateX(${-s}px)        translateY(-${totalRise * 0.50}px)`, offset: 0.50 },
            { opacity: 0.6, transform: `translateX(${-s * 0.2}px) translateY(-${totalRise * 0.64}px)`, offset: 0.64 },
            { opacity: 0.6, transform: `translateX(${s * 0.7}px)  translateY(-${totalRise * 0.78}px)`, offset: 0.78 },
            { opacity: 0.6, transform: `translateX(${s * 0.2}px)  translateY(-${totalRise * 0.92}px)`, offset: 0.92 },
            { opacity: 0,   transform: `translateX(0px)            translateY(-${totalRise}px)` }
        ]

        const anim = el.animate(keyframes, {
            duration,
            delay,
            easing: 'ease-in-out',
            fill: 'none'
        })

        anim.onfinish = () => el.remove()
    })
}

// --- DARK CARDS: Make entire card clickable ---
function initDarkCards() {
    const cards = document.querySelectorAll('.dark-card')

    cards.forEach(card => {
        card.addEventListener('click', () => {
            const link = card.querySelector('.card-link')
            if (!link) return

            // Check for data-url attribute first, fallback to link href
            const url = card.getAttribute('data-url') || link.getAttribute('href') || '#'
            window.location.href = url
        })

        // Add cursor pointer for better UX
        card.style.cursor = 'pointer'

        // Allow keyboard navigation (Enter key)
        card.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                card.click()
            }
        })
    })
}

