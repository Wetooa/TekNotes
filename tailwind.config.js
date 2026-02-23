/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    './**/templates/**/*.html',
    './static/**/*.js',
    '!./postgres_data/**',
    '!./node_modules/**',
  ],
  safelist: [
    // Course color variants used dynamically (bg-{{ course.color }}, text-{{ course.color }})
    { pattern: /^(bg|text|border)-(red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose|gray|slate|zinc|neutral|stone)-(50|100|200|300|400|500|600|700|800|900|950)$/ },
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
