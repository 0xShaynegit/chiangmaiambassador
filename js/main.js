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
    randomizePageFloats()
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

// NAVIGATION: Fixed at top, always visible
function initNavigation() {
    // Nav is positioned fixed at top via CSS, no scroll behavior needed
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

// RANDOMIZE: Page-wide floating lanterns get random positions and delays
function randomizePageFloats() {
    const pageFloats = document.querySelectorAll('.page-float')

    pageFloats.forEach((el, index) => {
        const randomLeft = Math.random() * 85 + 5
        const randomDelay = Math.random() * 4
        const randomDuration = 14 + Math.random() * 2

        el.style.left = randomLeft + '%'
        el.style.setProperty('--animation-delay', randomDelay + 's')
        el.style.setProperty('--animation-duration', randomDuration + 's')

        const animationString = `float-page linear ${randomDuration}s infinite, sway-page-${(index % 3) + 1} ${5 + Math.random() * 1.5}s ease-in-out infinite`
        el.style.animation = animationString
        el.style.animationDelay = randomDelay + 's'
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
