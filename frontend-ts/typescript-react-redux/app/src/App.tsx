import React from 'react';
import './App.css';

interface Props {

}

interface State {
  countries: any[];
  input: string;
}

class Card extends React.Component<{ name: string }> {
  render() {
    return (
      <div className='country-card'>
        {this.props.name}
      </div>
    );
  }
}

class App extends React.Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = {
      countries: [],
      input: '',
    };
  }

  componentDidMount() {
    fetch('https://restcountries.com/v2/all')
    .then(response => response.json())
    .then(data => {
      this.state.countries = data;
    });
  }

  render() {
    return (
      <div className="App">
        <h2>List of countries</h2>
        <input
          className='searchbar'
          placeholder={'Search countries...'}
          onChange={(e) => {
            this.setState({ input: e.target.value });
          }}
        />
        {
          this.state.countries.map(e => <Card name={e.name} />)
        }
      </div>
    );
  }
}

export default App;
