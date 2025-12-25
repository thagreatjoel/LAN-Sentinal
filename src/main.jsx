import React from 'react'
import ReactDOM from 'react-dom/client'
import { ThemeProvider } from 'theme-ui'
import theme from '@hackclub/theme'
import App from './App'

ReactDOM.createRoot(document.getElementById('root')).render(
  <ThemeProvider theme={theme} colorMode="dark">
    <App />
  </ThemeProvider>
)
