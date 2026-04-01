export interface ResultsList {
  score: number
  feedback: {
    warning: string
    suggestions: string[]
  }
  guesses: number
  crack_times_display: {
    [key: string]: string
  }
}
