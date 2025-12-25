import { Box } from 'theme-ui'
import Signup from './pages/Signup';

export default function App(){
  return(
    <Box bg="background" color="text" sx={{ minHeight: '100vh'}}>
    <Signup/>
    </Box>
  )
}
