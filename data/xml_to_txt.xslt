<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE xsl:stylesheet [<!ENTITY mdash "&#8212;"> ]>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="text" indent="yes" omit-xml-declaration="yes"/>
    <xsl:template match="/">
        <xsl:for-each select="timetable/dayOfWeek">
            <xsl:value-of select="@name"/>
            <xsl:text>&#xa;</xsl:text>
            <xsl:for-each select="subject">
                <xsl:value-of select="@start"/>
                <xsl:text> &mdash; </xsl:text>
                <xsl:value-of select="@end"/>
                <xsl:text>&#x9;</xsl:text>
                <xsl:value-of select="name"/>
                <xsl:value-of select="lecturer"/>
                <xsl:text>&#x9;</xsl:text>
                <xsl:value-of select="kind"/>
                <xsl:text>&#x9;</xsl:text>
                <xsl:value-of select="auditory"/>
                <xsl:text>&#x9;</xsl:text>
                <xsl:text>&#xa;</xsl:text>
            </xsl:for-each>
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>