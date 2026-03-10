/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./*.html",
    "./cv/*.html",
    "./certificates/*.html",
  ],
  theme: {
    extend: {
      colors: {
        bg:        '#0a0a0a',
        surface:   '#111111',
        surface2:  '#1a1a1a',
        surface3:  '#222222',
        accent:    '#00d4c8',
        'accent-dim': '#00a89e',
        'accent-glow': 'rgba(0,212,200,0.15)',
        text:      '#f0ede8',
        muted:     '#6b7280',
        'muted-2': '#9ca3af',
        border:    '#2a2a2a',
        'border-2':'#333333',
      },
      fontFamily: {
        display: ['Outfit', 'sans-serif'],
        body:    ['Outfit', 'sans-serif'],
      },
      fontSize: {
        'fluid-hero': 'clamp(3rem, 10vw, 8rem)',
        'fluid-h2':   'clamp(1.75rem, 4vw, 3rem)',
        'fluid-body': 'clamp(0.95rem, 2vw, 1.125rem)',
      },
      backgroundImage: {
        'noise': "url(\"data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E\")",
        'hero-glow': 'radial-gradient(ellipse 80% 60% at 50% -10%, rgba(0,212,200,0.12) 0%, transparent 70%)',
        'card-glow': 'radial-gradient(ellipse at top left, rgba(0,212,200,0.06), transparent 60%)',
      },
      boxShadow: {
        'accent': '0 0 30px rgba(0,212,200,0.2)',
        'card': '0 4px 24px rgba(0,0,0,0.4)',
        'card-hover': '0 8px 40px rgba(0,0,0,0.6), 0 0 0 1px rgba(0,212,200,0.2)',
      },
      keyframes: {
        fadeUp: {
          '0%':   { opacity: '0', transform: 'translateY(24px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        fadeIn: {
          '0%':   { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideInLeft: {
          '0%':   { opacity: '0', transform: 'translateX(-24px)' },
          '100%': { opacity: '1', transform: 'translateX(0)' },
        },
        pulse2: {
          '0%, 100%': { opacity: '1' },
          '50%':      { opacity: '0.5' },
        },
        marquee: {
          '0%':   { transform: 'translateX(0)' },
          '100%': { transform: 'translateX(-50%)' },
        },
      },
      animation: {
        'fade-up':       'fadeUp 0.6s ease forwards',
        'fade-in':       'fadeIn 0.5s ease forwards',
        'slide-in-left': 'slideInLeft 0.6s ease forwards',
        'pulse2':        'pulse2 2s ease-in-out infinite',
        'marquee':       'marquee 30s linear infinite',
      },
    },
  },
  plugins: [],
}
