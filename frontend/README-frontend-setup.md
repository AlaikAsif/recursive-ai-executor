Frontend setup notes

1. Install dependencies

   npm install

2. Tailwind setup

   - Ensure `postcss.config.cjs` and `tailwind.config.cjs` exist (they are included).
   - Add Tailwind directives to your main CSS (e.g., `src/index.css`):
     @tailwind base;
     @tailwind components;
     @tailwind utilities;

3. Run dev server

   npm run dev

4. If you prefer CRA scripts instead of Vite, you can use `npm start` (react-scripts).

Notes:
- `react-syntax-highlighter` is included for showing highlighted code. `highlight.js` is also added as an alternative.
- `concurrently` can be used to run frontend and backend together in dev scripts.
