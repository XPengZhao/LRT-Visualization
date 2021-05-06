import Time from "./timeClass"
const Tag = class {
    init() {
        this.timelist = {}
    }
    setValue(data){
        let timeArray = Date.parse(new Date(data.Time.slice(0,20)))
        let timeStamp = String(timeArray+data.Time.slice(20))
        let time = Time().setValue(data)
        this.timelist[timeStamp] = time
    }

}

export default Tag
