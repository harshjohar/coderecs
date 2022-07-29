/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    fontFamily: {
      poppins: ["poppins", 'sans-serif']
    },
    extend: {
      colors:{
        coderecs: {
            primary: "#ff77dd",
            hoverPrimary: "#eedd77",
            textLight: "#FFFFFF",
            textDark: "#05445E",
            bgDark: "#189AB4",
            bgLight: "#D4F1F4",
            bgNav: "#05445E"
        }
      }
    },
  },
  plugins: [
    require('tailwind-scrollbar-hide')
  ],
}
