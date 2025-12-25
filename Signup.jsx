import { Box, Button, Card, Heading, Text } from 'theme-ui'

export default function Signup() {
  return (
    <Box
      sx={{
        minHeight: '100vh',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        px: 3
      }}
    >
      <Card sx={{ width: '100%', maxWidth: 360 }}>
        <Heading variant="headline">HackaTime</Heading>
        <Text sx={{ color: 'muted', mb: 3 }}>
          Track your coding. Hack Club style.
        </Text>
        <Button variant="primary" sx={{ width: '100%' }}>
          Continue with Hack Club
        </Button>
      </Card>
    </Box>
  )
}
