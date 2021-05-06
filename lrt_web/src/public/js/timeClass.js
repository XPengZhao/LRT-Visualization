const Time = class {
    init() {
        this.attrlist = {}
    }
    setValue(data){
        this.Time = data.Time
        this.pos = data.pos
        this.phase = data.phase
        this.rss = data.rss
        this.spectrum = data.spectrum
    }
}

export default Time
