/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html"],
  safelist: [
    // Dynamic classes used in JS project card rendering
    'text-accent', 'text-purple-400', 'text-red-400',
    'bg-accent', 'bg-purple-400', 'bg-red-400',
    'hover:border-accent', 'hover:border-purple-400', 'hover:border-red-400',
    'hover:text-accent', 'hover:text-purple-400', 'hover:text-red-400',
    'bg-slate-900',
  ],
  theme: {
    extend: {
      colors: {
        primary: "#0f172a",
        card:    "#1e293b",
        accent:  "#38bdf8",
      }
    }
  },
  plugins: [],
}
