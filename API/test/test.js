require('chai').should();

app = require('../app.js')

describe('App test', () => {
  describe('Add Sequences',() => {
    it('should save a sequence', async function () {
      const fixtures = ['ATGC','CATCTGA','TCGAGTACGA']
      fixtures.forEach(app.add);

      app.sequences.should.have.members(fixtures)
    })
  })

  describe('Query Sequences',() => {
    it('should save a sequence', async function () {
      const fixtures = ['ATGCCATCTGATCGAGTACGA']
      const query = 'ATGCCATCTGATCGAGTATTT'
      fixtures.forEach(app.add);

      const result1 = app.find(query,3)
      const result2 = app.find(query,2)

      result1.should.eql(fixtures)
      result2.should.be.empty
    })
  })
})
