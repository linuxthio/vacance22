
class Menu
{
    constructor(x,y,titre,parent)
    {
        this.x=x;this.y=y;this.titre=titre;
        this.widget=document.createElement("div")
        this.parent=parent
        this.titre=titre
        this.widget.style.marginLeft="50%"
        this.widget.style.transform="translateX(-50%)"
        this.widget.style.fontSize=32+"px"
        this.widget.style.color="white"
        this.widget.innerHTML=titre
        this.parent.appendChild(this.widget)   
    }
    
    show(v)
    {
        this.widget.innerHTML=this.titre
        if (v===1)
        {
            this.widget.visible="box"
        }else
        {
            this.widget.visible="none"
        }
    }
}